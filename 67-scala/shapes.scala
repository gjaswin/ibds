// Abstract class with abstract and concrete methods
abstract class Shape {
// Abstract method
def area: Double
// Concrete method
def display(): Unit = {
println(s"Area of the shape: $area")
}
}
// Trait for coloring shapes
trait Colorable {
def color: String
def showColor(): Unit = {
println(s"The shape color is: $color")
}
}
// Concrete class Circle
class Circle(val radius: Double, val color: String) extends Shape with Colorable {
def area: Double = math.Pi * radius * radius
}
// Concrete class Rectangle
class Rectangle(val length: Double, val width: Double, val color: String) extends Shape
with Colorable {
def area: Double = length * width
}
// Main object
object AbstractAndTraitDemo {
def main(args: Array[String]): Unit = {
val circle = new Circle(5, "Red")
val rectangle = new Rectangle(4, 6, "Blue")
println("=== Circle ===")
circle.display()
circle.showColor()
println("\n=== Rectangle ===")
rectangle.display()
rectangle.showColor()
}
}
