object ImmutableCollectionsDemo {
  def main(args: Array[String]): Unit = {
    // 1. Immutable List
    val numbers = List(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    println(s"Original List: $numbers")

    // Using map to transform elements (double each number)
    val doubledNumbers = numbers.map(n => n * 2)
    println(s"Doubled List (map): $doubledNumbers")

    // Using filter to select elements (even numbers)
    val evenNumbers = numbers.filter(n => n % 2 == 0)
    println(s"Even Numbers (filter): $evenNumbers")

    // Using reduce to combine elements (sum of all numbers)
    val sum = numbers.reduce((a, b) => a + b)
    println(s"Sum of Numbers (reduce): $sum")

    // Using foldLeft to combine elements with an initial value (sum of numbers + 100)
    val sumWithInitial = numbers.foldLeft(100)((acc, n) => acc + n)
    println(s"Sum with initial value 100 (foldLeft): $sumWithInitial")

    // 2. Immutable Set
    val colors = Set("red", "green", "blue", "red", "yellow")
    println(s"Original Set: $colors")

    // Using map to transform elements (uppercase)
    val upperColors = colors.map(_.toUpperCase)
    println(s"Uppercase Colors (map): $upperColors")

    // Using filter to select elements (colors with length > 4)
    val longColors = colors.filter(_.length > 4)
    println(s"Colors with length > 4 (filter): $longColors")

    // 3. Immutable Map
    val ages = Map("Alice" -> 30, "Bob" -> 25, "Charlie" -> 35)
    println(s"Original Map: $ages")

    // Using map to transform values (increase age by 1)
    val increasedAges = ages.map { case (name, age) => name -> (age + 1) }
    println(s"Increased Ages (map): $increasedAges")

    // Using filter to select elements (people older than 30)
    val olderPeople = ages.filter { case (name, age) => age > 30 }
    println(s"Older People (filter): $olderPeople")

    // Using foldLeft to sum all ages
    val totalAge = ages.values.foldLeft(0)(_ + _)
    println(s"Total Age (foldLeft): $totalAge")

    // Sorting a list
    val unsortedList = List(5, 2, 8, 1, 9)
    val sortedList = unsortedList.sorted
    println(s"Unsorted List: $unsortedList")
    println(s"Sorted List: $sortedList")
  }
}