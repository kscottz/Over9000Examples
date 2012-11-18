// HELLO!
#include <iostream.h>
#include <string>
using namespace std;

int main(void)
{
  int i = 0; // This is -1 , 0, 1 2billion
  float j = 0.00; // -1.00 0.1232 1.123123
  string derp = "derp";
  int a = 0;

  cout << "Enter crap" << endl; // this let's me put it out. 
  cin >> a; // this let's me get info

  cout << "Hello World." << endl; 
  if( i > 9000 )
    {
      cout << "IT IS OVER 9000" << endl;
    }
  else
    {
      cout << "Lame" << endl; 
    }

  for( int k = 0; k < 100;k=k+2)
    {
      cout << "K is " << k << endl;
    }

  bool meow = false;

  
  while( !meow )
    {
      cout << "asdfasDF" << endl;
      meow = true;
    }
  cout << derp << endl;
  return 0;
}
