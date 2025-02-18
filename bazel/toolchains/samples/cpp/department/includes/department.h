#ifndef SAMPLE_DEPARTMENT_H
#define SAMPLE_DEPARTMENT_H

#include <string>

class Department
{

  public:
    Department(int id, std::string name, int employee_nu);
    int GetEmployeeNumber();
    int GetID();
    std::string GetName();

  private:
    int id;
    std::string name;
    int employee_nu;
};

#endif  // SAMPLE_DEPARTMENT_H
