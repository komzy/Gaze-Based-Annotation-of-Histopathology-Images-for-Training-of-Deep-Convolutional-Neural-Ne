import qupath.lib.geom.Point2
import qupath.lib.gui.QuPathGUI
import qupath.lib.roi.PointsROI
import qupath.lib.objects.PathAnnotationObject;
import qupath.lib.objects.classes.PathClassFactory
import qupath.lib.scripting.QPEx
import groovy.io.FileType

/* read CSVs level-wise that store gaze annotations and import to Qupath*/


def maxLevel=16 // SET THIS YOURSELF!

def imageData = QPEx.getCurrentImageData();
if (imageData == null) {
    print("No image open!");
    return
}

def server = imageData.getServer();
print("Current image name: " + imageData.getServer().getShortServerName());

def PixelWidthMicrons = imageData.getServer().getPixelWidthMicrons();
def PixelHeightMicrons= imageData.getServer().getPixelHeightMicrons();

// Prompt for directory containing csv
def dirCSV = QuPathGUI.getDialogHelper().promptForDirectory();
//def file2 = getQuPath().getDialogHelper().

def csvList = []
dirCSV.traverse(type: FileType.FILES, maxDepth: 0, nameFilter: ~/.*[0-9]\.csv/) { csvList << it }

csvList.each {
    def file = new File(it.path)
// Create BufferedReader
def csvReader = new BufferedReader(new FileReader(file));
def fileName = file.getName()
    print fileName
def level = fileName.replaceAll("[^0-9]", "").toInteger()

def count=0;
def scalingFactor = 2 ** (maxLevel-level)
List<Point2> points = [];

// Loop through all the rows of the CSV file.
while ((row = csvReader.readLine()) != null) {

    def rowContent = row.split(",")
    double cx = rowContent[0] as double;
    double cy = rowContent[1] as double;

     cx = cx * scalingFactor
     cy = cy * scalingFactor

    points.add(new Point2(cx,cy))
    count++;
}
def roi = new PointsROI(points)
def annotation = new PathAnnotationObject(roi, PathClassFactory.getPathClass("Level "+level));
imageData.getHierarchy().addPathObject(annotation, false);
}
print "Done!"