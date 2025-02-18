#ifndef SAMPLE_COMPANY_H
#define SAMPLE_COMPANY_H

#include "department.h"
#include <list>
#include <optional>
#include <vector>

class Company
{

  public:
    explicit Company(std::string name);
    std::string GetName();
    void AddDepartment(int id, std::string dep_name, int employee_nu);
    std::optional<Department> GetDepartmentByName(const std::string& name);
    size_t GetNumberOfDepartments();

  private:
    std::string name;
    std::list<Department> departments;
};

#endif  // SAMPLE_COMPANY_H
