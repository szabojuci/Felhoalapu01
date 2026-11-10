using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;

namespace WebAPI.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class PizzaController : ControllerBase
    {
        public static List<string> pizzas = new List<string> { "Margherita", "Pepperoni", "Hawaiian" };
        [HttpGet]
        public IActionResult GetPizzas()
        {

            return Ok(pizzas);
        }

        [HttpPost]

        public IActionResult AddPizza(string pizzaName)
        {
            if (string.IsNullOrEmpty(pizzaName))
            {
                return BadRequest("Pizza name cannot be empty.");
            }
            else
            {
                pizzas.Add(pizzaName);
                return Ok($"Pizza '{pizzaName}' added successfully.");
            }
        }

        [HttpPut]

        public IActionResult UpdatePizza(string oldPizzaName, string newPizzaName)
        {
            if (string.IsNullOrEmpty(oldPizzaName) || string.IsNullOrEmpty(newPizzaName))
            {
                return BadRequest("Both old and new pizza names must be provided.");
            }
            if (oldPizzaName == newPizzaName)
            {
                return BadRequest("The new pizza name must be different from the old pizza name.");
            }
            else
            {
                if (pizzas.Contains(oldPizzaName))
                {
                    pizzas[pizzas.IndexOf(oldPizzaName)] = newPizzaName;
                    return Ok($"Pizza '{oldPizzaName}' updated to '{newPizzaName}'.");
                }
                else
                {
                    return NotFound($"Pizza '{oldPizzaName}' not found.");
                }
            }
        }

        [HttpDelete]

        public IActionResult DeletePizza(string pizzaName)
        {
            if (string.IsNullOrEmpty(pizzaName))
            {
                return BadRequest("Pizza name cannot be empty.");
            }
            else
            {
                if (pizzas.Contains(pizzaName))
                {
                    pizzas.Remove(pizzaName);
                    return Ok($"Pizza '{pizzaName}' deleted successfully.");
                }
                else
                {
                    return NotFound($"Pizza '{pizzaName}' not found.");
                }
            }
        }
    }
}
