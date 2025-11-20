// Abstract class Vehicle
abstract class Vehicle {
def move(): Unit // abstract method
def stop(): Unit = {
println("Vehicle stopped") }
}
// Subclass Bike
class Bike extends Vehicle {
def move(): Unit = println("The bike is moving on two wheels")
}
// Subclass Car
class Car extends Vehicle {
def move(): Unit = println("The car is moving on four wheels")
}
// Main object
object VehicleDemo {
def main(args: Array[String]): Unit = {
val bike = new Bike()
val car = new Car()
bike.move()
bike.stop()
car.move()
car.stop()
}
}
