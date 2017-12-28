#include <iostream>
int main() 
{
  int A = 0, B = 0, C = 0, moves = 0, place = 0;
	std::cin >> A >> B >> C;
	while (B - A > 1 or C - B > 1) {
	  if (B - A > C - B) {
			C = B - 1;
			place = B;
			B = C;
			C = place;
			++moves;
	  } else {
			A = B + 1;
			place = B;
			B = A;
			A = place;
			moves++;
		}
  }
std::cout << moves << std::endl;
return 0;
}
