#include "UIEngine.hpp"
#include <iostream>
#include <memory>
#include <string>

extern "C++" {
std::unique_ptr<ui::UIEngine> get_ui_engine()
{
    std::cout << "Hello from ui engine" << std::endl;
    return std::make_unique<ui::UIEngine>();
}
}
