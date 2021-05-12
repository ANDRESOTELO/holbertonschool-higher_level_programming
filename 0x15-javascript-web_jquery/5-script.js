/*
adds a <li> element to a list when the user clicks on the tag #add_item
*/
$('#add_item').click(function () {
  const addItem = '<li>Item</li>';
  $('UL.my_list').append(addItem);
});
