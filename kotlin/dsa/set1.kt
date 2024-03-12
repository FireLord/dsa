fun main() {
    val s = "A man, a plan, a canal: Panama"
    println(isPalindrome(s))
}

fun isPalindrome(s: String): String {
    val str = mutableListOf<Char>()
    for (i in 0 until s.length){
        if (s[i].isLetter()){
            str.add(s[i].toLowerCase())
         } else {
            continue
        }
    }
    val result = str.joinToString("")
    return result
    // if (result==s){
    //     return true
    // } else {
    //     return false
    // }
}