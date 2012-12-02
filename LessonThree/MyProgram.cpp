#include "derp.h"
#include <iostream>

using namespace std;
int main(void)
{
  Derp jake(0,0);
  int lightyear = 3;
//   cout << "----------------" << endl;
//   for( int i = 2; i < 10; i=i+2)
//     {
//       cout << "i: " << i << endl;
//     }
//   cout << "----------------" << endl;
//   for( int i = 0; i <= 10; i++)
//     {
//       cout << "i: " << i << endl;
//     }
//   cout << "----------------" << endl;
//   for( int i = 10; i > 0; i--)
//     {
//       cout << "i: " << i << endl;
//     }
//   cout << "WE ARE GETTING CRAZY" << endl;
//   cout << "----------------" << endl;
 
  for( int i = 0; i < 100; i++ ) // <-- THIS IS EASIER TO READ AND FASTER
    {
      cout << "i: " << i << endl;
      jake.makeJakeFall(lightyear);
      jake.makeJakeGoForward(2);
      jake.whereTheFIsJake();
    }
  return 0;
}
