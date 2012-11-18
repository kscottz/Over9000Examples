// HELLO!
#include <iostream.h>
#include <string>
using namespace std;

// This is a function that checks if a
// number is over 9000 and returns a 
// string


string IsThisOver9000( int a )
{
  string ReturnThisString = "";
  if( a > 9000 )
    {
      ReturnThisString = "IT IS OVER 9000!";
    }
  else
    {
      ReturnThisString = "NOT OVER 9000";
    }
  return ReturnThisString;
}

int doStuff(int i)
{
  int j = 10;
  j = j+1;
  cout << "My J " << j << endl;
  return 0;
}

int main(void)
{
  int a = 12;
  for( int i=0; i < 10; i++ )
    {
      int j = 43;
      cout << "j " << j << endl;
      j = j + 1;
      cout << "j " << j << endl;
      doStuff(j);
      cout << "END OF THE LOOP" << endl;
    }
}
