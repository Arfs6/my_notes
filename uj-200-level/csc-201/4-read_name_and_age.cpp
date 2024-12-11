// Read name and age
#include "std_lib_facilities.h"

int main() {
	cout << "Please enter your first name and age\n"; // Prompt message
	int age; // Integer variable
	string first_name; // string variable
	cin >> first_name; // input into string variable
	cin >> age; // Input into int variable
	cout << "Hello, " << first_name << " (age " << age << ")\n";
	// Greeting message with int variable.
}
