
function getContextURL() {
	var pageUrl = '';
	var topLocationHref = '';

	try {
		topLocationHref = top.location.href;
	}
	catch (e) {}
	var documentReferrer = "";
	try {
		documentReferrer = document.referrer;
	}
	catch (e) {}
	var documentLocationHref = "";
	try {
		documentLocationHref = document.location.href;
	}
	catch (e) {}

	if (parent !== window) {
		if (topLocationHref !== undefined && topLocationHref !== '') {
			pageUrl = topLocationHref;
		}
		else if (documentReferrer !== undefined && documentReferrer !== '') {
			pageUrl = documentReferrer;
		}
		else {
			pageUrl = documentLocationHref;
		}
	}
	else {
		pageUrl = documentLocationHref;
	}

	return pageUrl;
}

function firePixel(pixel) {
	if (pixel === '')
		return;

	var img = new Image();
	img.src = pixel;
}

function loadJSTag(jsTag, parentNode) {
	if (jsTag === '')
		return;

	var script = document.createElement("script");
	script.type = "text/javascript";
	script.src = jsTag;
	parentNode.parentNode.insertBefore(script, parentNode);
}

var afURL = 'https://t.us1.dyntrk.com/spfban.php?dynk=sma4rt4bt4fg&dynt=73&a=104916&cp=124351&c=257017&cd=0&td=215&kl=06010022-651039038114484884771800000025701723092415&id=1&ic=CL&ir=BI&dma=-1&zip=4030775&city=concepcion&afbu={ADFRAUD_PAGE_URL}&blk=1&cb=169556198726380';
var contextURL = getContextURL();

if (afURL !== '') {
	afURL = afURL.replace('{ADFRAUD_PAGE_URL}', encodeURIComponent(contextURL));

	var meScript		= document.currentScript;
	var mediaContent	= (meScript.hasAttribute('data-media-content')	? atob(meScript.getAttribute('data-media-content')) : '');
	var mediaWidth		= (meScript.hasAttribute('data-media-width')	? meScript.getAttribute('data-media-width')		: '');
	var mediaHeight		= (meScript.hasAttribute('data-media-height')	? meScript.getAttribute('data-media-height')	: '');

	var afXHR = new XMLHttpRequest();
	afXHR.timeout = 10000;

	afXHR.addEventListener("load", function(event) {
		if (mediaContent !== "" && afXHR.status === 200) {
			var iframe = document.createElement('iframe');
			iframe.style.border		= '0';
			iframe.style.margin		= '0';
			iframe.style.padding	= '0';
			iframe.style.overflow	= 'hidden';
			iframe.style.display	= 'block';
			iframe.width			= mediaWidth;
			iframe.height			= mediaHeight;
			iframe.scrolling		= 'no';
			meScript.parentNode.insertBefore(iframe, meScript);
			iframe.contentWindow.contents = mediaContent;
			iframe.src = 'javascript:window["contents"]';
		}
		else {
			firePixel('https://t.us1.dyntrk.com/t.php?dynk=sma4rt4bt4fg&dynt=3&a=104916&cp=124351&c=257017&cd=0&td=215&kl=06010022-651039038114484884771800000025701723092415&id=1&ic=CL&ir=BI&dma=-1&zip=4030775&city=concepcion&bm=I05yIpY4Va_6pjkpeEWGtEcigQw2RuSSVPg9pw&g=1-3205945_48272&wpc=USD&dynbi=&cb=169556198726380');
					}
	});

	afXHR.addEventListener("error", function(event) {
		firePixel('https://t.us1.dyntrk.com/t.php?dynk=sma4rt4bt4fg&dynt=3&a=104916&cp=124351&c=257017&cd=0&td=215&kl=06010022-651039038114484884771800000025701723092415&id=1&ic=CL&ir=BI&dma=-1&zip=4030775&city=concepcion&bm=I05yIpY4Va_6pjkpeEWGtEcigQw2RuSSVPg9pw&g=1-3205945_48272&wpc=USD&dynbi=&cb=169556198726380');
	});

	afXHR.open("GET", afURL);
	afXHR.send();
}


