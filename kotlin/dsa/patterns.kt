fun main() {
    val n = readLine()!!.toInt()
    // pattern1(n)
    // pattern2(n)
    // pattern3(n)
    // pattern4(n)
    // pattern5(n)
    // pattern6(n)
    // pattern7(n)
    // pattern8(n)
    // pattern9(n)
    // pattern10(n)
    pattern11(n)
    // pattern12(n)
}

private fun pattern1(n: Int) {
    for (i in 1..n) {
        for (j in 1..n) {
            print("* ")
        }
        println()
    }
}

private fun pattern2(n: Int) {
    for (i in 1..n) {
        for (j in 1..i) {
            print("* ")
        }
        println()
    }
}

private fun pattern3(n: Int) {
    for (i in 1..n) {
        for (j in 1..i) {
            print("$j ")
        }
        println()
    }
}

private fun pattern4(n: Int) {
    for (i in 1..n) {
        for (j in 1..i) {
            print("$i ")
        }
        println()
    }
}

private fun pattern5(n: Int) {
    for (i in n downTo 1) {
        for (j in i downTo 1) {
            print("* ")
        }
        println()
    }
}

private fun pattern6(n: Int) {
    for (i in n downTo 1) {
        for (j in 1..i) {
            print("$j ")
        }
        println()
    }
}

private fun pattern7(n: Int) {
    for (i in 0 until n) {
        for (j in 0 until (n-i-1)) {
            print(" ")
        }

        for (k in 0 until (2*i+1)) {
            print("*")
        }

        for (l in 0 until (n-i-1)) {
            print(" ")
        }
        println()
    }
}

private fun pattern8(n: Int) {
    for (i in (n-1) downTo 0) {
        for (j in 0 until (n-i-1)) {
            print(" ")
        }

        for (k in 0 until (2*i+1)) {
            print("*")
        }

        for (l in 0 until (n-i-1)) {
            print(" ")
        }
        println()
    }
}

private fun pattern9(n: Int) {
    for (i in 0 until n) {
        for (j in 0 until (n-i-1)) {
            print(" ")
        }

        for (k in 0 until (2*i+1)) {
            print("*")
        }

        for (l in 0 until (n-i-1)) {
            print(" ")
        }
        println()
    }

    for (i in (n-1) downTo 0) {
        for (j in 0 until (n-i-1)) {
            print(" ")
        }

        for (k in 0 until (2*i+1)) {
            print("*")
        }

        for (l in 0 until (n-i-1)) {
            print(" ")
        }
        println()
    }
}

private fun pattern10(n: Int) {
    for (i in 1..(2*n-1)) {
        var stars = i
        if (i > n) stars = 2*n-i
        for (j in 1..stars) {
            print("*")
        }
        println()
    }
}

private fun pattern11(n: Int) {
    var start = 1
    for (i in 0 until n) {
        if (i % 2 == 0) start = 0 else start = 1
        for (j in 0..i) {
            print(start)
            start = 1 - start
        }
        println()
    }
}

private fun pattern12(n: Int) {

}