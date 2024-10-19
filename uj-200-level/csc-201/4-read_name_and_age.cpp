// Read name and age
#include "std_lib_facilities.h"

int main() {
	cout << "Please enter your first name and age\n";
	int age; // Integer variable
	string first_name;
	cin >> first_name;
	cin >> age;
	cout << "Hello, " << first_name << " (age " << age << ")\n";
}
