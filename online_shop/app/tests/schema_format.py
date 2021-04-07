category_list_query = """
query{
      allCategories{
        name
        id
      }
    }
"""

single_category_query = """

    query{
      category(id: 1) {
        id
        name
      }
    }

"""

create_category_mutation = """
     mutation createCategory($name: String) {
        createCategory(name: $name){
            category{
                name
            }
        }
  }

"""

update_category_mutation = """
    mutation updateCategory($name: String, $id: ID){
        updateCategory(name: $name, id: $id)
        {
            category{
                name
                id
            }
        }
    }
"""

delete_category_mutation = """
    mutation deleteCategory($id: ID!) {
        deleteCategory(id: $id) {
            ok
        }
    }
"""

# ================================= For product modules =====================
product_query_list = """
    query{
      allProducts{
          id
          name
          price
          category{
            id
            name
          }
      inStock
      }
    }
"""

