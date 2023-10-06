#include <iostream>
#include <map>
#include <iomanip>
using namespace std;

int main() {
  // Empty dictionary
  map<string, int> grades;
  char check;
  int grade;
  bool exit = false;
  
  //Gather user input until they quit
  cout <<  "(A)dd, (R)emove, (M)odify, (P)rint all, or (Q)uit? ";
  cin >> check;
  check = toupper(check);
  
  // Boolean controlled while loop
  while (!exit) {
  // Add name and grade to the dictionary or give error
   if (check == 'A') 
   {
     string name;
     cout << "Enter the name of the student: ";
     cin >> name;
     auto it = grades.find(name);
     if(it != grades.end()) {
          cout << "Sorry, that student is already present ";
          continue;
     }
     cout << "Enter the student's grade: ";
     cin >> grade;
     grades[name] = grade;
     cout << "(A)dd, (R)emove, (M)odify, (P)rint all, or (Q)uit? ";
     cin >> check;
     check = toupper(check);
   } 

    // Remove a student from the query or give an error  
    else if (check == 'R') {
      string erase;
      cout << "What student do you want to erase? ";
      cin >> erase;
      auto it = grades.find(erase);
      if (it != grades.end()) {
        grades.erase(it);
      }
      else {
        cout << "Sorry, that student doesn't exist and couldn't be removed.";
        continue;
      }
      cout << "(A)dd, (R)emove, (M)odify, (P)rint all, or (Q)uit? ";
     cin >> check;
     check = toupper(check);
    }

    // Modify a student's grade if they exist
  else if(check == 'M') {
    string mod;
    int newG;
    cout << "Enter the name of the student you want to modify: ";
    cin>> mod;
    auto it = grades.find(mod);
        if (it != grades.end()) {
          cout << "The old grade is " << grades[mod] << endl;
          cout << "Enter new grade: ";
    cin >> newG;
    grades[mod] = newG;
          cout << "(A)dd, (R)emove, (M)odify, (P)rint all, or (Q)uit? ";
     cin >> check;
     check = toupper(check);
        }
      else {
        cout << "Sorry, that student doesn't exist and could not be modified" << endl;
        continue;
      }
  }

    // Print the average grade and list the students: grades
  else if(check == 'P') {
    double total = 0;
    double count = grades.size();
    for (const auto& pair : grades) {
      total += pair.second;
    }
    double avg = total / count;
    cout << "The average is " << fixed << setprecision(2) << avg << endl;
    for (const auto& pair : grades) {
      cout << pair.first << ": " << pair.second << endl;
    }
    cout << "(A)dd, (R)emove, (M)odify, (P)rint all, or (Q)uit? ";
     cin >> check;
     check = toupper(check);
  }
    
    // User terminates program, program says goodbye
    else if (check == 'Q') {
      cout << "Goodbye!";
      exit = true;
    }
      
    // Ensures the user enters the right letter options
    else {
      cout << "Sorry, that wasn't a valid choice" << endl;
      cout << "(A)dd, (R)emove, (M)odify, (P)rint all, or (Q)uit? ";
     cin >> check;
     check = toupper(check);
    }
}
  return 0;
}