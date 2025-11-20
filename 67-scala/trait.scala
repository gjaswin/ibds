// Abstract class Vehicle
abstract class Vehicle {
def move(): Unit
def stop(): Unit = {
println("Vehicle stopped")
}
}
// Subclass Bike
class Bike extends Vehicle {
def move(): Unit = println("The bike is moving on two wheels")
}
// Subclass Car
class Car extends Vehicle {
def move(): Unit = println("The car is moving on four wheels")
}
// Trait for insurance
trait Insurable {
def insuranceAmount: Double
def printInsurance(): Unit = {
println(s"Insurance amount: $$${insuranceAmount}")
}
}
// Extend Car and Bike with Insurable trait
class InsuredBike extends Bike with Insurable {
def insuranceAmount: Double = 5000.0
}
class InsuredCar extends Car with Insurable {
def insuranceAmount: Double = 20000.0
}
// Main object
object InsuranceDemo {
def main(args: Array[String]): Unit = {
val bike = new InsuredBike()
val car = new InsuredCar()
bike.move()
bike.printInsurance()
car.move()
car.printInsurance()
}
}
