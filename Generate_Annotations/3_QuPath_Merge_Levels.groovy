import qupath.lib.geom.Point2
import qupath.lib.gui.QuPathGUI
import qupath.lib.roi.PointsROI
import qupath.lib.objects.PathAnnotationObject;
import qupath.lib.objects.classes.PathClassFactory
import qupath.lib.scripting.QPEx
import groovy.io.FileType

/* Combine all individual levels to one level (maximum level) and save in CSV*/


def maxLevel=16  // SET THIS YOURSELF!

List<Point2> points = [];

def imageData = QPEx.getCurrentImageData();
if (imageData == null) {
    print("No image open!");
    return
}

for (annotation in getAnnotationObjects()) {
    roi = annotation.getROI()
    List<Point2> copypoints = roi.getPointList()
    copypoints.each {
        points.add(new Point2(it.x, it.y))
    }

}
print points.size()
removeObjects(getAnnotationObjects(),true)
def roi2 = new PointsROI(points)
def newAnnotation = new PathAnnotationObject(roi2, PathClassFactory.getPathClass("All Annotations"));
imageData.getHierarchy().addPathObject(newAnnotation, false);

def dirCSV = QuPathGUI.getDialogHelper().promptForDirectory().toString()


def file = new File(dirCSV + "\\Level " + maxLevel + ".csv")
    if (file.isFile() || !file.createNewFile()) {
        println "Failed to create file: $file"
        return
    }

points.each {
        cx = Math.round(it.x.toInteger())
        cy = Math.round(it.y.toInteger())
        file.append(cx.toString() + "," + cy.toString() + "\n")
    }

print "Done!"