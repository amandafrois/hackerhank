# Pytest 
# Mobile

from proj.inventory import MobileInventory, InsufficientException
import pytest
 
 
class TestingInventoryCreation:
    def test_creating_empty_inventory(self):
        c1 = MobileInventory({})
        assert c1.balanced_inventory == {}
 
    def test_creating_specified_inventory(self):
        c2 = MobileInventory(
            {"iPhone Model X": 100, "Xiaomi Model Y": 1000, "Nokia Model Z": 25}
        )
        assert c2.balanced_inventory == {
            "iPhone Model X": 100,
            "Xiaomi Model Y": 1000,
            "Nokia Model Z": 25,
        }
 
    def test_creating_inventory_with_list(self):
        with pytest.raises(TypeError) as excinfo:
            c3 = MobileInventory(["iPhone Model X", "Xiaomi Model Y", "Nokia Model Z"])
        assert "Input inventory must be a dictionary" in str(excinfo.value)
 
    def test_creating_inventory_with_numeric_keys(self):
        with pytest.raises(ValueError) as excinfo:
            c4 = MobileInventory(
                {1: "iPhone Model X", 2: "Xiaomi Model Y", 3: "Nokia Model Z"}
            )
        assert "Mobile model name must be a string" in str(excinfo.value)
 
    def test_creating_inventory_with_nonnumeric_values(self):
        with pytest.raises(ValueError) as excinfo:
            c5 = MobileInventory(
                {
                    "iPhone Model X": "100",
                    "Xiaomi Model Y": "1000",
                    "Nokia Model Z": "25",
                }
            )
        assert "No. of mobiles must be a positive integer" in str(excinfo.value)
 
    def test_creating_inventory_with_negative_value(self):
        with pytest.raises(ValueError) as excinfo:
            c6 = MobileInventory(
                {"iPhone Model X": -45, "Xiaomi Model Y": 200, "Nokia Model Z": 25}
            )
        assert "No. of mobiles must be a positive integer" in str(excinfo.value)
