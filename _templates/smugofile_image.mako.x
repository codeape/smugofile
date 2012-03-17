## Template for the page that show the image

<%inherit file="site.mako" />

## An url back to the photo album index
<a href="/${gallery_path}/index.html">Gallery index</a>

<h1>${photo["image_name"]}</h1>
<br />
## An url to a thumb sized image located at SmugMug
<img src="${photo["url_thumb"]}" alt="${photo["image_id"]}" /><br />

## An url to a tiny sized image located at SmugMug
<img src="${photo["url_tiny"]}" alt="${photo["image_id"]}" /><br />

## An url to a small sized image located at SmugMug
<img src="${photo["url_small"]}" alt="${photo["image_id"]}" /><br />

## An url to a medium sized image located at SmugMug
<img src="${photo["url_medium"]}" alt="${photo["image_id"]}" /><br />

## An url to a large sized image located at SmugMug
<img src="${photo["url_large"]}" alt="${photo["image_id"]}" /><br />

## An url to a xlarge sized image located at SmugMug
<img src="${photo["url_xlarge"]}" alt="${photo["image_id"]}" /><br />

## An url to a xxlarge sized image located at SmugMug
<img src="${photo["url_x2large"]}" alt="${photo["image_id"]}" /><br />

## An url to a xxxlarge sized image located at SmugMug
<img src="${photo["url_x3large"]}" alt="${photo["image_id"]}" /><br />

## An url to a original sized image located at SmugMug
<img src="${photo["url_original"]}" alt="${photo["image_id"]}" /><br />
