#include <iostream>

#include "company.h"

int main(int /* argc */, char** /* argv */)
{

    Company awesome_company("SuperAwesome Inc.");
    std::cout << "Company name: " << awesome_company.GetName() << '\n';

    awesome_company.AddDepartment(13, "QX-57", 26262);  // NOLINT(cppcoreguidelines-avoid-magic-numbers)

    auto department = awesome_company.GetDepartmentByName("QX-57");
    if (department)
    {
        std::cout << "Department ID: " << department->GetID() << '\n';
    }

    return 0;
}
