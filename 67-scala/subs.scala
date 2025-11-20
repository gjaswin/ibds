val subjects = Set("Math", "Science", "English", "Math") // duplicates auto-removed
val studentMarks = Map("Alice" -> 67, "Bob" -> 45, "Charlie" -> 89, "David" -> 32, "Eve"
-> 76)
// Highest and lowest marks
val highest = studentMarks.values.max
val lowest = studentMarks.values.min
println(s"Subjects: $subjects")
println(s"Student Marks: $studentMarks")
println(s"Highest Mark: $highest")
println(s"Lowest Mark: $lowest")
