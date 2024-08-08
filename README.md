# Annotator Labelling Instructions

## Assembling your files

Please consult the [RAITE Annotator Assignment](https://docs.google.com/spreadsheets/d/1OOpkYjrd_0YWI4ENj9j83rmngUwbK_TZB3Vg4ajRInM/edit?gid=640096086#gid=640096086) Google Sheet to see your assignments. 

You will be assigned a match, round, segment, and confidence level. The path to your assigned JSON and video files are denoted under the `JSON File Path` and `Video File Path` column in the sheet. Please note that there is one video file for each pair of confidence levels. Save all the files to the machine that you will be using to annotate. 

For the local storage set-up of Label Studio to function properly the video file should be saved in a folder named `data` anywhere on your machine, but keep note of the absolute path where it is stored.

## Installing Label Studio

Create and activate a virtual environment.

### Anaconda Environment Creation Example
```
conda create --name label-studio
conda activate label-studio
```

### Install with pip

```
pip install -U label-studio
label-studio
```

### Install with Anaconda

```
conda install psycopg2
pip install label-studio
label-studio
```

Label Studio should now launch. Log in or create an account on the page that opens.

## Creating the project

1. Select `Create` and name the project. The name doesn't matter.

![image](https://github.com/zachvin/labelling-instructions/blob/0d1c1b252e9ca8426f8a481f241811ac0622a228/label_studio_create.png)

2. On the top, select `Labeling Setup`, then `Videos` on the left, then `Video object tracking`.

![image](https://github.com/zachvin/labelling-instructions/blob/9308fd1d08c10eacff063a530d027fc6f62a5ea7/label_studio_label_setup.png)

3. Click on `Code` and *replace* the text in the box with the following snippet. 

```
<View>
  <Header value="RAITE Annotating"/>
  <Text name="" value="Your annotation interface is ready. Use the &quot;person&quot; label to 
                       annotation all instances in which a person is present in the video." />
  <Labels name="videoLabels" toName="video" allowEmpty="true">
    <Label value="person" background="#F45866"/>
  </Labels>
  <Video name="video" value="$video" framerate="30"/>
  <VideoRectangle name="box" toName="video"/>
</View>
```

**If you miss this step, your labelling interface will not contain the correct labels and annotations will appear to lag behind the video.**

![image](https://github.com/zachvin/labelling-instructions/blob/9308fd1d08c10eacff063a530d027fc6f62a5ea7/label_studio_code_setup.png)

3. Click `Save`. You should be at the annotation task screen now.

![image](https://github.com/zachvin/labelling-instructions/blob/9308fd1d08c10eacff063a530d027fc6f62a5ea7/label_studio_save.png)

4. Since your project doesn't have any data you will be prompted to import some. Use either `Import` button to begin the process of importing one or more videos.

![image]([label_studio_import_data.png](https://github.com/zachvin/labelling-instructions/blob/107bea95ed2430636c3362ad0616368ef1bd43c4/label_studio_import_data.png))

5. To start, select the `Upload Files` button and select the three samples videos.

![image](https://github.com/zachvin/labelling-instructions/blob/107bea95ed2430636c3362ad0616368ef1bd43c4/label_studio_upload_files.png)

5. Once they have finished processing click the `Import` button on the top right.

![image](https://github.com/zachvin/labelling-instructions/blob/107bea95ed2430636c3362ad0616368ef1bd43c4/label_studio_processed_files.png)

6.  You should be returned to the main project screen and see a task entry for each sample videos file. Clicking the `Show task source` button will allow you to see information about the task.

![image](https://github.com/zachvin/labelling-instructions/blob/208157791c06e673380bd9bbb26e4f2e16cef400/label_studio_show_task.png) 

   Click on one of the tasks to begin annotating.


**If you have any problems, please reach out to Zach Vincent (zvincent@nd.edu) or Benjamin Sporrer (bsporrer@nd.edu) via email or on Slack.**

## Annotating

### Video instructions

For a video demonstration of the labeling process please view this [video](https://www.youtube.com/watch?v=Y4Ngy96UH_Q).

### Text instructions

Label Studio annotation is straightforward. Please label all people in in each video. If you would not be able to identify an object as a person in that frame, then do not label it.

* Move, resize, and delete existing bounding boxes by clicking on a box and dragging or pressing backspace.

* Label Studio uses a keypoint interpolation system to display bounding boxes on the screen even when no bounding box is explicity specified. This interpolation moves the box linearly between keypoints and can either help or hinder the annotation process. You can enable/disable interpolation between two keyframes with the `Toggle interpolation` button below.

  ![trimmedinterpolation](https://github.com/zachvin/labelling-instructions/assets/43306216/c19a0eba-aafb-4e95-864f-0c9e243d15ab)

* Deleting a bounding box deletes all the bounding boxes associated with that object for all future and past frames. For this reason, it's best only to delete bounding boxes if your are absolutely sure. `Ctrl+Z` does usually work to undo accidental deletions.

* To delete a bounding box for a single frame, use the `Toggle keypoint` button. You can also use this button to turn an interpolated or nonexistent bounding box into a keypoint.

  ![image](https://github.com/zachvin/labelling-instructions/assets/43306216/f16dbe5b-ffd9-421a-8350-f484e3799233)

* The above image also shows the main Label Studio tools for navigating the video.

* When creating a new bounding box, be sure to label it as a person by selecting it then either clicking on `person` on the top of the screen or pressing the hotkey associated with that class (mine is 1, and yours likely will be as well).

* Generally speaking, try to extend previously existing bounding boxes and do not create new ones. In the event that a person is recognized for a few frames but that recognition is dropped, click on the bounding box in a frame where it exists, navigate to the next frame where it does not exist, and use the `Toggle keypoint` button to make it appear. This way we can avoid making too many unique IDs.

* There may be some instances where a person may be labeled as `person_X` but several frames later becomes `person_Y`. This is not a problem. Use whichever ID is easiest to label with according to the note above.

* When you're done, click `Update` to save your annotations.

## Saving your Annotations

* The project overview screen includes an `Export` button. Unfortunately, the default functionality of Lable Studio and the functionality of that button will only export keyframe annotation data. Any interpolated frames will not be included in an export if the `Export` button is used.

**DO NOT USE THE `EXPORT` BUTTON TO EXPORT YOUR RESULTS.**

* Instead we'll be utilizing the following python script to export the annotations. This script work via [Label Studio SDK](https://github.com/HumanSignal/label-studio-sdk), which is installed autmatically when installing Label Studio. If for some reason it isn't installed the follow command should install it properly.

```
pip install --upgrade label-studio-sdk
```

# Label Studio Export Script (also a file in thie github repo)
```
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
```

* You can either pull the file from github or copy the contents seen here into a new file. Once copied three variables will need to be replaced: `YOUR_API_KEY`, `PROJECT_ID`, and `path/to/output`.

* The `YOUR_API_KEY` needs to be replaced with your specific API key. While keeping the terminal running Lable Studio active open a web browser and type or paste `http://localhost:8080/api/current-user/token` into the address bar. As long as Label Studio is running this will return your individual API key. Copy the API key value and paste it into the script in place of `YOUR_API_KEY`.

* The `PROJECT_ID` can be found in a similar way. With a Label Studio instance running type or paste `http://localhost:8080/api/projects/` into a browser's address bar. This will display the metadata of all your projects. Look for the title of the project that needs exported. The project's id will be right before it. Copy or type tht project's id into the `PROJECT_ID` field.

![image](https://github.com/zachvin/labelling-instructions/blob/3853b778a555165aba370c92862078cef16a3a6b/label_studio_project_idpng.png)

* The `path/to/output` variable should be set to the directory in which you wish to save the exported annotation. The generated project file will include output for every task in the project, so an export only needs to be done once.

* Once the annotation file has been generated please save it the Google Drive located 












* Use   includes an Go back to the project overview screen and select `Export` and export the project in JSON format. Please rename the file based on your match, round, segment, and confidence intervals in this format: `match10r1_seg2_yd0.2_annotated.json` and upload to `/afs/crc.nd.edu/group/cvrl/czajka/crane3/raite/annotators/completed`. Thank you for your help!
