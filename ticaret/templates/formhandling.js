function myfun(ev)
{
    ev.preventDefault();
    console.log("data submitted");
var x=document.getElementById('name').value;
var y=document.getElementById('gender').value;
console.log(x);
console.log(y);
}