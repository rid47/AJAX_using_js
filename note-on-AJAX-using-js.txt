document.addEventListener('DOMContentLoaded', () =>{



	document.querySelector('#form').onsubmit = () =>{


		//Initializa new request
		const request = new XMLHttpRequest();
		const city = document.querySelector("#city").value;
		request.open('POST', '/get_weather');

		// Callback function for when request completes

		request.onload = ()=>{

			const data = JSON.parse(request.responseText);
			if(data.success){
			const contents = `Temperature: ${data.temperature} degree`;
			document.querySelector('.card-text').innerHTML = contents;
			document.querySelector('.card-subtitle').innerHTML = data.description;
		}
		else{
			document.querySelector('.card-text').innerHTML = 'There was an error.';	
			document.querySelector('.card-subtitle').innerHTML = ' ';
		}


		}

		// Add data to send with request
		const data = new FormData();
		data.append('mycity', city);
		request.send(data);
		return false;

	}
})