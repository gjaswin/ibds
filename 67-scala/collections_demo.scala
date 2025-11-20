
object CollectionsDemo extends App {

  val numbersList = List(1, 5, 2, 8, 3, 7, 4, 6)
  println(s"Original List: $numbersList")

  val doubledList = numbersList.map(_ * 2)
  println(s"List after doubling each element (map): $doubledList")

  val evenNumbersList = numbersList.filter(_ % 2 == 0)
  println(s"List with only even numbers (filter): $evenNumbersList")

  val sumWithReduce = numbersList.reduce(_ + _)
  println(s"Sum of list elements (reduce): $sumWithReduce")

  val sumWithFold = numbersList.fold(10)(_ + _)
  println(s"Sum of list elements with initial value 10 (fold): $sumWithFold")

  val sortedList = numbersList.sorted
  println(s"Sorted list: $sortedList")
  
  val transformedList = numbersList.filter(_ > 3).map(_ * 3).sorted
  println(s"Chained operations (filter > 3, map * 3, sorted): $transformedList")


  val fruitsSet = Set("apple", "banana", "cherry", "date", "apple")
  println(s"Original Set: $fruitsSet")

  val uppercaseSet = fruitsSet.map(_.toUpperCase)
  println(s"Set with uppercase strings (map): $uppercaseSet")

  val longNameFruits = fruitsSet.filter(_.length > 5)
  println(s"Set with fruits having length > 5 (filter): $longNameFruits")


  val studentGrades = Map("Alice" -> 85, "Bob" -> 92, "Charlie" -> 78, "David" -> 95)
  println(s"Original Map: $studentGrades")

  val updatedGrades = studentGrades.map { case (name, grade) => (name, grade + 5) }
  println(s"Map with grades increased by 5 (map): $updatedGrades")

  val topStudents = studentGrades.filter { case (_, grade) => grade > 90 }
  println(s"Map with students scoring > 90 (filter): $topStudents")
  
  val topStudentNames = studentGrades.filter(_._2 > 90).keys
  println(s"Names of top students: $topStudentNames")
}
