#include <iostream>

using namespace std;

class Position
{
 public:
  int x;
  int y;
};

////////////////////////////////////////////////////////////
////////////////////////// THIS IS FRIGGIN MAGIC ///////////
////////////////////////////////////////////////////////////
class Derp
{

 public:
  Position jakes_position;
  int gravity; 

  Derp(int j_x, int j_y)
  {
    gravity = -10; // the center of the earth is -infinity    
    jakes_position.x = j_x;
    jakes_position.y = j_y;
  }

  void makeJakeFall(int time)
  {
    jakes_position.y += gravity*time;
  }
  
  void makeJakeGoForward( int distance )
  {
    jakes_position.x += distance;
  }
  
  void whereTheFIsJake(void)
  {
    cout << "Jake is at " << "(" << jakes_position.x << "," << jakes_position.y << ")" << endl;
  }
};
////////////////////////////////////////////////////////////
