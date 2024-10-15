# Annotator Labelling Instructions

<!-- Commenting out file downloading instructions as we will be providing annotators with the videos.

## Downloading the files

The files we need are located in the following two directories on the CRC: `/afs/crc.nd.edu/group/cvrl/czajka/crane3/raite/dataset` and `/afs/crc.nd.edu/group/cvrl/czajka/crane3/raite/samples`. The `dataset` subdirectory contains the entire dataset consisting of the full length videos. The `samples` directory contains three one minutes clips curated from different videos.

Please copy the entirty of the `samples` directory to your local machine (the one you are planning to run Label Studio on). You can copy the entirty of both directories to your machine if you choose, but do not need to as you'll only need to copy the full length videos that you choose to be the annotator of.

<!-- Commenting out DVC instructions since it was causing permission errors. Need to fix later.

To download the video files we will be utilizing the RAITE [data registry](https://dvc.org/doc/use-cases/data-registry). It is a [DVC](https://dvc.org/) repository that contains the dataset, metadata, and samples of the videos for training and calibrating.

To install DVC and download the dataset, please see the usage example [repository](https://github.com/nd-crane/raite-data-registry-usage-example). This GitHub repo provides all the details needed to install and download the datasets.

You will need to download both the `dataset` and `sample` directories. Example commands to do so are outline in the DVC usage repository. More specific ones are located below for quick reference.

###### Local (From within a CRC machine)

If you are logged into a CRC machine at the University of Notre Dame you can use the following commands.

```bash
dvc get https://github.com/nd-crane/raite-data-registry data/raite_2023/dataset
dvc get https://github.com/nd-crane/raite-data-registry data/raite_2023/samples
```

###### Remote SSH to a CRC machine

If you are on your local machine and connected to the Notre Dame VPN you can add the flag `--remote` to specify `cvrl_remote` as a remote location. If doing this make sure you set-up a local DVC configuration file with your CRC username. Then add the `--config` flag with the path to your local configuration file. 

The default path from within a DVC repository is `./.dvc/config.local`. This is used in the example below.

```bash
dvc get --remote cvrl_remote --config ./.dvc/config.local https://github.com/nd-crane/raite-data-registry data/raite_2023/dataset
dvc get --remote cvrl_remote --config ./.dvc/config.local https://github.com/nd-crane/raite-data-registry data/raite_2023/samples
```

###### Google Drive

If you don't have access to CRC machines at the University of Notre Dame, add the flag `--remote` to specify `gdrive` as a remote location. See the example below.

```bash
dvc get --remote gdrive https://github.com/nd-crane/raite-data-registry data/raite_2023/dataset
dvc get --remote gdrive https://github.com/nd-crane/raite-data-registry data/raite_2023/samples
```
-->

## Annotation Assignments

We are asking everyone to begin by annotating the three sample videos. This will help to familiarize you will Label Studio, the various types of attacks seen in the dataset, set annotator baselines, and ensure there are no issues with the instructions.

**Please complete the annotations for the three sample videos in their entirety by following these instructions through to the end (including uploading your results) before moving on to an actual full length video.**

It is recommended to create two projects in Label Studio. One for the sample videos and one for the match videos. You can create more if you like (e.g. one per actual video), but making at least two is recommended due to the nature of exporting the results.

<!--  Once you have completed the sample annotation videos please consult the [RAITE Annotating](https://docs.google.com/spreadsheets/d/1edHaBMsEwN22dWU_nhGDCEAo8vy0214Dov-BVVsCR2s/edit?gid=0#gid=0) Google Sheet to select and checkout full match videos. Make sure to update the `Annotator` column with your name upon checkout. You do not need to upload your completed annotations upon finishing one video if you plan to do more. This is especially true if using a single project as every task in a given project is exported everytime. Meaning subsequent exports would contain duplicate annotations. Please do mark remmber to mark the sheet with your name when you decide to annotate a video and to put a checkmark in the appropriate boxes to update statuses.  

-->

## Installing Label Studio

Create and activate a virtual environment.

##### Anaconda environment creation example
```
conda create --name labelStudio
conda activate labelStudio
```

##### Install with pip and launch

```
pip install -U label-studio
label-studio
```

##### Install with Anaconda and launch

```
conda install psycopg2
pip install label-studio
label-studio
```

Label Studio should now launch. Log in or create an account on the page that opens.

If you have any issues the official [Label Studio Requirements](https://labelstud.io/guide/install_requirements#:~:text=Server%20requirements,but%2016GB%20RAM%20is%20recommended) may be able to help.

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
                       annotate all instances in which a person is present in the video." />
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

![image](https://github.com/zachvin/labelling-instructions/blob/3d5fca5391bdcb8fc77b49609cedfd1dd9d8d013/label_studio_import_data.png)

5. To start, select the `Upload Files` button and select the three samples videos.

![image](https://github.com/zachvin/labelling-instructions/blob/107bea95ed2430636c3362ad0616368ef1bd43c4/label_studio_upload_files.png)

5. Once they have finished processing click the `Import` button on the top right.

![image](https://github.com/zachvin/labelling-instructions/blob/107bea95ed2430636c3362ad0616368ef1bd43c4/label_studio_processed_files.png)

6.  You should be returned to the main project screen and see a task entry for each sample videos file. Clicking the `Show task source` button will allow you to see information about the task.

![image](https://github.com/zachvin/labelling-instructions/blob/208157791c06e673380bd9bbb26e4f2e16cef400/label_studio_show_task.png) 

   Click on one of the tasks to begin annotating.


**If you have any problems, please reach out to Benjamin Sporrer (bsporrer@nd.edu) via email.**

## Annotating

### Video instructions

For a video demonstration of the labeling process please view this [video](https://www.youtube.com/watch?v=pMbNVEoPiy4).

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

* The project overview screen includes an `Export` button. Unfortunately, the default functionality of Label Studio will cause exporting via that button to only export keyframe annotation data. Any interpolated frames will not be included in an export if the `Export` button is used.

**DO NOT USE THE `EXPORT` BUTTON TO EXPORT YOUR RESULTS.**

* Instead we'll be utilizing the following python script to export the annotations. This script works via [Label Studio SDK](https://github.com/HumanSignal/label-studio-sdk), which is installed automatically when installing Label Studio. If for some reason it isn't installed the following command should install it properly.

```
pip install --upgrade label-studio-sdk
```

##### Label Studio Export Script (also a file in this GitHub repo)

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

* You can either pull the file from GitHub or copy the contents seen here into a new file.

* Open a new terminal to work on the file while keeping the one running Label studio active. There are three variables that will need to be replaced: `YOUR_API_KEY`, `PROJECT_ID`, and `path/to/output`.

* The `YOUR_API_KEY` variable needs to be replaced with your specific API key. While keeping the terminal running Label Studio active open a web browser and type or paste `http://localhost:8080/api/current-user/token` into the address bar. As long as Label Studio is running this will return your individual API key. Copy the API key value and paste it into the script in place of `YOUR_API_KEY`.

* The `PROJECT_ID` can be found in a similar way. With a Label Studio instance running type or paste `http://localhost:8080/api/projects/` into a browser's address bar. This will display the metadata of all your projects. Look for the title of the project that needs exported. The project's id will be right before it. Copy or type the project's id into the `PROJECT_ID` field.

![image](https://github.com/zachvin/labelling-instructions/blob/3853b778a555165aba370c92862078cef16a3a6b/label_studio_project_idpng.png)

* The `path/to/output` variable should be set to the directory in which you wish to save the exported annotation. The generated project file will include output for every task in the project, so an export only needs to be done once per project.

* Runing the script will generate an output file of the following format `project-id-at-YYYY-MM-DD-HH-MM-UniqueID`. Please rename this file by replacing the project information with your name and by removing the unique ID so that it is of the form `yourName-YYYY-MM-DD-HH-MM`. In the case of the sample videos please add `samples` to the end so that it is of the form `yourName-YYYY-MM-DD-HH-MM-samples`.

<!--
* Once the annotation file has been renamed please upload it to the Google Drive located [here](https://drive.google.com/drive/u/1/folders/0ANt-j76-H8d9Uk9PVA?role=writer). If you lack permission to access the drive please send a request and permission will be granted.
-->

* Once the annotation file has been renamed please email it to Benjamin Sporrer (bsporrer@nd.edu) with the subject line RAITE Annotation.

**Thank you again for your help!**
