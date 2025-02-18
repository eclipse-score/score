#include "department.h"

#include <utility>

Department::Department(int id, std::string name, int employee_nu)
    : id(id), name(std::move(name)), employee_nu(employee_nu) {};

int Department::GetEmployeeNumber()
{
    return this->employee_nu;
}

std::string Department::GetName()
{
    return this->name;
}

int Department::GetID()
{
    return this->id;
}
