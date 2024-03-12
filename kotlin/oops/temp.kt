open class Foo {
    open fun test(){
        println("Hello world!")
    }
}

class Foo1: Foo(){
    override fun test(){
        println("ff")
    }
}

fun main() {
    val temp = Foo1()
    temp.test()
}