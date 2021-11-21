import qupath.lib.geom.Point2
import qupath.lib.gui.QuPathGUI
import qupath.lib.roi.PointsROI
import qupath.lib.objects.PathAnnotationObject;
import qupath.lib.objects.classes.PathClassFactory
import qupath.lib.scripting.QPEx
import groovy.io.FileType

def dirCSV = QuPathGUI.getDialogHelper().promptForDirectory().toString()

def maxLevel=16

for (annotation in getAnnotationObjects()) {
    roi = annotation.getROI()
    pathClass = annotation.getPathClass().toString()
    def level = pathClass.replaceAll("[^0-9]", "").toInteger()
    def scalingFactor = 2 ** (maxLevel-level)
    def file = new File(dirCSV+"\\"+pathClass+".csv")

    if (file.isFile() || !file.createNewFile()) {
        println "Failed to create file: $file"
        return
    }
    
    List<Point2> points = roi.getPointList()
    points.each {
        cx = Math.round(it.x.toInteger() / scalingFactor)
        cy = Math.round(it.y.toInteger() / scalingFactor)
        file.append(cx.toString()+","+cy.toString()+"\n")
    }

}
print "Done!"
