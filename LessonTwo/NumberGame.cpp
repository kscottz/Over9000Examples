// HELLO!
#include <iostream.h>
#include <string>
using namespace std;

// This is a function that checks if a
// number is over 9000 and returns a 
// string

bool CheckNumber( int MyNumber, int Guess )
{
  bool returnValue = false;
  if ( Guess == MyNumber )
    {
      returnValue = true;
      cout << "You guessed the number right" << endl;
    }
  else if( Guess < MyNumber )
    {
      cout << "Your number is too small" << endl;
    }
  else
    {
      cout << "Your guess was too high" << endl;
    }
  return returnValue;
}
int main(void)
{
  int MyNumber = 42;
  bool IsDone = false;
  while ( !IsDone )
    {
      cout << "Guess a number" << endl;
      int Guess;
      cin >> Guess;
      cout << "You chose " << Guess << endl;
      IsDone = CheckNumber( MyNumber, Guess);
    }
  return 0;
}
