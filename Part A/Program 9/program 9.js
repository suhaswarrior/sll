function LetterSurround(str)
{
    //Invalid conditions
    if(str.length==0) return "Invalid Entry"; //Empty string
  if(str[0]>='a' || str[str.length-1]>='a') //First or last character is not a letter
        return false; //Invalid
    for(i=1;i<str.length-1;i++) 
    {
        if(str[i]>='a') //If any character is not a letter
        {
            if(str[i-1]!='+'||str[i+1]!='+') //If the character is not surrounded by '+'
                return false;
        }
     }
     return true;
}  
function check()
{
document.getElementById('result').innerHTML=LetterSurround(document.getElementById('input').value); //Display result
}