# Pytest 
# Mobile

class TestInventoryAddStock(): 

  def setup_class(cls):
         cls.inventory = MobileInventory({'iPhone Model X': 100, 'Xiaomi Model Y': 1000, 'Nokia Model Z':25})
 
  def test_add_new_stock_as_dict(self):
         with pytest.raises(TypeError) :
             MobileInventory.add_stock(['iPhone Model X', 'Xiaomi Model Y', 'Nokia Model Z'])
 

def test_add_new_stock_as_list(self):
       with pytest.raises(TypeError) as excinfo:
             MobileInventory(['iPhone Model X', 'Xiaomi Model Y', 'Nokia Model Z'])
        assert "Input inventory must be a dictionary" in str(excinfo.value)
 
def test_add_new_stock_with_numeric_keys(self):
       with pytest.raises(ValueError) as excinfo:
              MobileInventory({1:'iPhone Model A', 2:'Xiaomi Model B', 3:'Nokia Model C'})
       assert "Mobile model name must be a string" in str(excinfo.value)

def test_add_new_stock_with_nonnumeric_values(self):
      with pytest.raises(ValueError) as excinfo:
            MobileInventory({'iPhone Model A':'50', 'Xiaomi Model B': '2000', 'Nokia ModelC':'25'})
      assert "No. of mobiles must be a positive integer" in str(excinfo.value)

def test_add_new_stock_with_float_values(self):
       with pytest.raises(ValueError) as excinfo:
             MobileInventory({'iPhone Model A':50.5, 'Xiaomi Model B':2000.3, 'Nokia Model C':25})
       assert "No. of mobiles must be a positive integer" in str(excinfo.value)



class TestInventorySellStock:

    inventory = None

    @classmethod
    def setup_class(cls):
        cls.inventory = MobileInventory(
            {
                "iPhone Model A": 50,
                "Xiaomi Model B": 2000,
                "Nokia Model C": 10,
                "Sony Model D": 1,
            }
        )

    def test_sell_stock_as_dict(self):
        self.inventory.sell_stock(
            {"iPhone Model A": 2, "Xiaomi Model B": 20, "Sony Model D": 1}
        )

    def test_sell_stock_as_list(self):
        with pytest.raises(TypeError):
            MobileInventory.sell_stock(
                self, ["iPhone Model A", "Xiaomi Model B", "Nokia Model C"]
            )

    def test_sell_stock_with_numeric_keys(self):
        with pytest.raises(ValueError):
            MobileInventory.sell_stock(
                self, {1: "iPhone Model A", 2: "Xiaomi Model B", 3: "Nokia Model C"}
            )

    def test_sell_stock_with_nonnumeric_values(self):
        with pytest.raises(ValueError):
            MobileInventory.sell_stock(
                self,
                {"iPhone Model A": "5", "Xiaomi Model B": "3", "Nokia Model C": "4"},
            )

    def test_sell_stock_of_nonexisting_model(self):
        with pytest.raises(InsufficientException, match="No Stock. New Model Request"):
            self.inventory.sell_stock({"iPhone Model B": 2, "Xiaomi Model B": 5})

    def test_sell_stock_of_insufficient_stock(self):
        with pytest.raises(InsufficientException, match="Insufficient Stock"):
            self.inventory.sell_stock(
                {"iPhone Model A": 2, "Xiaomi Model B": 5, "Nokia Model C": 15}
            )

