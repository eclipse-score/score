#include <gtest/gtest.h>

TEST(HelloTest, BasicAssertions)
{
    const int i = 42;
    EXPECT_EQ(i, 42);
}
