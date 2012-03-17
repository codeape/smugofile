## Template for the index of photo albums

<%inherit file="site.mako" />

## List all photo albums
% for gallery in galleries:
        <a href="/${root_path}/${gallery["album_id"]}/index.html">
        % if len(gallery["images"]) > 0:
                <img src="${gallery["images"][0]["url_thumb"]}" alt="${gallery["album_id"]} /">
        % else:
                <b>[ No thumbs in gallery ]</b>
        % endif
        ${gallery["album_title"]}
        (${len(gallery["images"])} photos)
        </a>
        </br>
% endfor

