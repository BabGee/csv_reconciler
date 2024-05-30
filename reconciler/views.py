from django.shortcuts import render
import csv
import io
from django.http import HttpResponse
from reconciler.forms import CSVUploadForm

def reconcile_csv(source_file, target_file):
    source_data = {}
    target_data = {}

    # Read source CSV
    source_csv = io.StringIO(source_file.read().decode('utf-8'))
    reader = csv.DictReader(source_csv)
    for row in reader:
        #print(f'ROW>>>>>>{row}')
        source_data[row['ID']] = row 

    # Read target CSV
    target_csv = io.StringIO(target_file.read().decode('utf-8'))
    reader = csv.DictReader(target_csv)
    for row in reader:
        target_data[row['ID']] = row

    missing_in_target = []
    missing_in_source = []
    field_discrepancies = []

    # Check for records in source but not in target
    for key in source_data:
        if key not in target_data:
            missing_in_target.append(key)

    # Check for records in target but not in source
    for key in target_data:
        if key not in source_data:
            missing_in_source.append(key)

    # Check for discrepancies in records present in both files
    for key in source_data:
        if key in target_data:
            discrepancies = {}
            for field in source_data[key]:
                if source_data[key][field] != target_data[key][field]:
                    discrepancies[field] = (source_data[key][field], target_data[key][field])
            if discrepancies:
                field_discrepancies.append((key, discrepancies))

    return missing_in_target, missing_in_source, field_discrepancies

def upload_csv(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            source_file = form.cleaned_data['source_file']
            target_file = form.cleaned_data['target_file']
            missing_in_target, missing_in_source, field_discrepancies = reconcile_csv(source_file, target_file)

            # Generate CSV response
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="reconciliation_report.csv"'
            writer = csv.writer(response)
            writer.writerow(['Type', 'Record Identifier', 'Field', 'Source Value', 'Target Value'])

            for id in missing_in_target:
                writer.writerow(['Missing in Target', id, '', '', ''])

            for id in missing_in_source:
                writer.writerow(['Missing in Source', id, '', '', ''])

            for id, discrepancies in field_discrepancies:
                for field, values in discrepancies.items():
                    writer.writerow(['Field Discrepancy', id, field, values[0], values[1]])

            return response
    else:
        form = CSVUploadForm()
    return render(request, 'reconciler/upload.html', {'form': form})
