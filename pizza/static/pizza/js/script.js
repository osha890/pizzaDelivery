$(document).ready(function () {
  // Форма добавления пиццы в корзину
  $('#add-to-cart-form').on('submit', function (event) {
    event.preventDefault()

    var pizzaId = $(this).find('input[name="pizza_id"]').val()
    var quantity = $(this).find('input[name="quantity"]').val()

    $.ajax({
      url: "{% url 'cart:add_to_cart' %}",
      method: 'POST',
      data: {
        pizza_id: pizzaId,
        quantity: quantity,
        csrfmiddlewaretoken: '{{ csrf_token }}',
      },
      success: function (response) {
        // Обновите корзину на странице без перезагрузки
        updateCartUI(response)
      },
      error: function (response) {
        console.error(response)
      },
    })
  })

  // Обновление количества элементов в корзине
  $('.update-cart-item').on('change', function (event) {
    var itemId = $(this).data('item-id')
    var quantity = $(this).val()

    $.ajax({
      url: "{% url 'cart:update_cart_item' %}",
      method: 'POST',
      data: {
        item_id: itemId,
        quantity: quantity,
        csrfmiddlewaretoken: '{{ csrf_token }}',
      },
      success: function (response) {
        // Обновите корзину на странице без перезагрузки
        updateCartUI(response)
      },
      error: function (response) {
        console.error(response)
      },
    })
  })
})

// Функция для обновления UI корзины
function updateCartUI(data) {
  // Пример: обновление количества и цены в корзине
  var itemRow = $('#cart-item-' + data.id)
  itemRow.find('.item-quantity').text(data.quantity)
  itemRow.find('.item-total-price').text(data.quantity * data.pizza.price)

  // Также обновите общую сумму и другие элементы корзины
}
