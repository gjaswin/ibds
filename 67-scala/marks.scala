val marks = List(45, 67, 89, 32, 76)
// Square of each mark
val squaredMarks = marks.map(m => m * m)
// Marks greater than 50
val above50 = marks.filter(_ > 50)
// Sum of marks
val total = marks.foldLeft(0)(_ + _)
println(s"Original Marks: $marks")
println(s"Squared Marks: $squaredMarks")
println(s"Marks > 50: $above50")
println(s"Total Marks: $total")
