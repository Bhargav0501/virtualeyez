/*const synth = window.speechSynthesis;

const form = document.querySelector('form');
const textarea = document.getElementById('maintext');
const voice_select = document.getElementById('voice-select');
const rate = document.getElementById('rate');
const pitch = document.getElementById('pitch');
const rateval = document.getElementById('rate-value');
const pitchval = document.getElementById('pitch-value');*/

// let voices = [];
/*

const getVoice = () => {

	voices = synth.getVoices();
	var option_string = "";
	voices.forEach(value => {
		var option = value.name + ' (' + value.lang + ') ';
		var newOption = "<option data-name='" + value.name +
				"' data-lang='" + value.lang + "'>" + option
				+ "</option>\n";
		option_string += newOption;
	});

	voice_select.innerHTML = option_string;
}

synth.onvoiceschanged = function() {
	getVoice();
};

const speak = () => {

	if(synth.speaking) {
		alert('Already speaking....');
		return;
	}

	if(textarea.value !== '') {

		const speakText = new SpeechSynthesisUtterance(textarea.value);

		speakText.onend = e => {
			console.log('Speaking is done!');
		};

		speakText.error = e=> {
			console.error('Error occured...');
		};

		const id = voice_select.selectedIndex;
		const selectedVoice =
			voice_select.selectedOptions[0].getAttribute('data-name');

		voices.forEach(voice => {
			if(voice.name === selectedVoice) {
				speakText.voice = voice;
			}
		});
		if(selectedVoice == undefined || speakText.voice === undefined){
			speakText.voice = voices[0]
		}
		speakText.rate = rate.value;
		speakText.pitch = pitch.value;

		synth.speak(speakText);
	}
};

rate.addEventListener('change', evt => rateval.innerHTML
		= (Number.parseFloat(rate.value) * 10) + "");

pitch.addEventListener('change', evt => pitchval.innerHTML
		= (Number.parseFloat(pitch.value) * 10) + "");

form.addEventListener('submit', evt => {
	evt.preventDefault();
	speak();
	textarea.blur();
});
*/
const synth = window.speechSynthesis;

const inputForm = document.querySelector('form');
const inputTxt = document.querySelector('#maintext');
const voiceSelect = document.querySelector('#voice-select');

const pitch = document.querySelector('#pitch');
const pitchValue = document.querySelector('.pitch-value');
const rate = document.querySelector('#rate');
const rateValue = document.querySelector('.rate-value');

let voices = [];

function populateVoiceList() {
  voices = synth.getVoices();

  for(var i = 0; i < voices.length ; i++) {
    var option = document.createElement('option');
    option.textContent = voices[i].name + ' (' + voices[i].lang + ')';

    if(voices[i].default) {
      option.textContent += ' -- DEFAULT';
    }

    option.setAttribute('data-lang', voices[i].lang);
    option.setAttribute('data-name', voices[i].name);
    voiceSelect.appendChild(option);
  }
}

populateVoiceList();
if (speechSynthesis.onvoiceschanged !== undefined) {
  speechSynthesis.onvoiceschanged = populateVoiceList;
}

inputForm.onsubmit = function(event) {
  event.preventDefault();

  var utterThis = new SpeechSynthesisUtterance(inputTxt.value);
  var selectedOption = voiceSelect.selectedOptions[0].getAttribute('data-name');
  for(var i = 0; i < voices.length ; i++) {
    if(voices[i].name === selectedOption) {
      utterThis.voice = voices[i];
    }
  }
  utterThis.pitch = pitch.value;
  utterThis.rate = rate.value;
  synth.speak(utterThis);

  inputTxt.blur();
}