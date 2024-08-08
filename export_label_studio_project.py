from label_studio_sdk import Client

# Initialize the client
ls = Client(url='http://localhost:8080', api_key='YOUR_API_KEY')
project = ls.get_project(PROJECT_ID)

# Create the export snapshot
snapshot_response = project.export_snapshot_create(title='Export with interpolation', interpolate_key_frames=True)

# Extract the snapshot_id from the dictionary
snapshot_id = snapshot_response.get('id')
print(f"Snapshot ID: {snapshot_id}")

# Download the export file
try:
    status_code, filename = project.export_snapshot_download(snapshot_id, export_type="JSON", path='/path/to/output')
    if status_code == 200:
        print(f"Export downloaded successfully: {filename}")
    else:
        print(f"Failed to download export. Status code: {status_code}")
except Exception as e:
    print(f"An error occurred: {e}")
