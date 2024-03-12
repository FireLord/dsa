fun main(){
    val myLambda:(Int, Int)->Int = {x,y -> x+y}
    addTwoNum(5, 6, myLambda)
}

fun addTwoNum(a:Int,b:Int,myFunc:(Int, Int)->Int){
    var result = myFunc(a,b)
    print(result)
}