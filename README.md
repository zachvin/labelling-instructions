# labelling-instructions

## Annotator instructions

### Installing Label Studio

Create and activate a virtual environment. Note that `LABEL_STUDIO_LOCAL_FILES_DOCUMENT_ROOT` must be the *direct parent folder* of the `data` folder in which your video is stored.

```
pip install -U label-studio
export LABEL_STUDIO_LOCAL_FILES_SERVING_ENABLED=true
export LABEL_STUDIO_LOCAL_FILES_DOCUMENT_ROOT=/home/user/path/to/folder/
label-studio
```

Label Studio should now launch. Log in or create an account on the page that opens.

### Creating the project

1. Select `Create` and name the project. The name doesn't matter.

2. On the top, select `Labeling Setup`, then `Videos` on the left, then `Video object tracking`. Click on `Code` and *replace* the text in the box with the following snippet. If you miss this step, the bounding boxes will not be the correct color and will appear to lag behind the video.

```
<View>
  <Header value="Great!" />
  <Text name="" value="Your labels are good to go. All people will be outlined in the red color below, and other recognitions will be in gray." />
  <Labels name="videoLabels" toName="video" allowEmpty="true">
    <Label value="person" background="#F45866"/>
  </Labels>
  <Video name="video" value="$video" framerate="30"/>
  <VideoRectangle name="box" toName="video"/>
</View>
```

3. Click `Save`. You should be at the annotation task screen now.

4. On the top right, select `Settings` then `Cloud Storage`. Select `Add Source Storage`.

5. Choose `Local Storage` from the `Storage Type` dropdown.

6. `Storage Title` can be anything. You will not need to remember it.

7. Your `Absolute local path` **must be a direct subdirectory** of `LABEL_STUDIO_LOCAL_FILES_DOCUMENT_ROOT` and also must end in `/data`. For example, my complete path is `/home/zach/projects/annotation/data` and my document root is `/home/zach/projects/annotation`. Use `Check Connection` to make sure everything is working properly.

> Common errors include forgetting to set the document root and not making the absolute local path a subdirectory of the root.

```
annotation
└── data
    └── match9r1_seg0.mp4
```

8. Go back to the annotator screen by clicking the project name on the top of the screen and click `Go to import`. Here, select the JSON file you were given to annotate and click `Import`. Additionally, make sure the associated video is moved to the `data` folder. If the video appears as expected, then you're good to start annotating. If you have any problems, reach out to Zach Vincent or Ben Sporrer on Slack.

## Annotating

Label Studio annotation is straightforward. Please label all people in your 2-minute segment. If you would not be able to identify an object as a person in that frame, then do not label it. Move, resize, and delete existing bounding boxes by clicking on a box and dragging or pressing backspace. Label Studio uses a keypoint interpolation system to display bounding boxes on the screen even when no bounding box was explicity specified. This interpolation moves the box linearly between keypoints and can either help or hinder the annotation process. You can enable/disable interpolation with the `Toggle interpolation` button below.

![trimmedinterpolation](https://github.com/zachvin/labelling-instructions/assets/43306216/c19a0eba-aafb-4e95-864f-0c9e243d15ab)

* Deleting a bounding box deletes all the bounding boxes associated with that object for all future and past frames. For this reason, it's best only to delete bounding boxes associated with objects of the wrong class (i.e. don't delete people). `Ctrl+Z` does usually work to undo accidental deletions.

* To delete a bounding box for a single frame, use the `Toggle keypoint` button. You can also use this button to turn an interpolated frame into a keypoint frame.

  ![image](https://github.com/zachvin/labelling-instructions/assets/43306216/f16dbe5b-ffd9-421a-8350-f484e3799233)

* The above image also shows the main Label Studio tools for navigating the video.

* If you are creating a new bounding box, be sure to label it as a person by selecting it then either clicking on `person` on the top of the screen or pressing the hotkey associated with that class (mine is 2, and yours likely will be as well).

* Generally speaking, try to extend previously existing bounding boxes and do not create new ones. In the event that a person is recognized for a few frames but that recognition is dropped, click on the bounding box in a frame where it exists, navigate to the next frame where it does not exist, and use the `Toggle keypoint` button to make it appear. This way we can avoid making too many unique IDs.

* There may be some instances where a person may be labeled as `person_X` but several frames later becomes `person_Y`.
