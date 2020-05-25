/*!
 * bootstrap-fileinput v4.4.7
 * http://plugins.krajee.com/file-input
 *
 * Font Awesome icon theme configuration for bootstrap-fileinput. Requires font awesome assets to be loaded.
 *
 * Author: Kartik Visweswaran
 * Copyright: 2014 - 2018, Kartik Visweswaran, Krajee.com
 *
 * Licensed under the BSD 3-Clause
 * https://github.com/kartik-v/bootstrap-fileinput/blob/master/LICENSE.md
 */
(function ($) {
    "use strict";

    $.fn.fileinputThemes.fa = {
        fileActionSettings: {
            showUpload: false,
            showZoom: false,
            removeIcon: '<i class="fa fa-trash"></i>',
            indicatorSuccess: '<i class="fa fa-check-circle text-success"></i>',
            indicatorError: '<i class="fa fa-exclamation-circle text-danger"></i>',
            indicatorLoading: '<i class="fa fa-hourglass text-muted"></i>'
        },
        layoutTemplates: {
            fileIcon: '<i class="fa fa-file kv-caption-icon"></i> '
        },
        previewFileIcon: '<i class="fa fa-file"></i>',
        browseIcon: '<i class="fa fa-folder-open"></i>',
        removeIcon: '<i class="fa fa-trash"></i>',
        cancelIcon: '<i class="fa fa-ban"></i>',
        uploadIcon: '<i class="fa fa-upload"></i>',
        msgValidationErrorIcon: '<i class="fa fa-exclamation-circle"></i> '
    };
})(window.jQuery);

$("#files").fileinput({
    theme: 'fa',
    uploadUrl: '#',
    allowedFileExtensions: ['docx'],
    overwriteInitial: false,
    slugCallback: function (filename) {
        return filename.replace('(', '_').replace(']', '_');
    }
});

$("#files1").fileinput({
    theme: 'fa',
    uploadUrl: '#',
    allowedFileExtensions: ['docx'],
    overwriteInitial: false,
    slugCallback: function (filename) {
        return filename.replace('(', '_').replace(']', '_');
    }
});