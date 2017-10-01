var channel_list = {};

for (var i=0; i < document.getElementsByTagName('ul')[2].children.length; i++) {
  var channelInformation = document.getElementsByTagName('ul')[2].children[i];
  var channelNumber = channelInformation.innerText.split(' ')[0];
  var channelName = channelInformation.innerText.split(' ').splice(1).join(' ');
  channel_list[channelName] = channelNumber;
}
