import os
import zipfile
import re
import shutil

root_path = "C:\\Users\\benbe\\Desktop"
file_path = "Compressed"
temp_path = "TempUncomp"
comp_path = "Completed"


def fix():
        pagefile_re = re.compile("page\\d*.xhtml")
        error_re = re.compile("<br>")
        for file in os.listdir(os.path.join(root_path, file_path)):
                if file.endswith(".epub") or file.endswith(".zip"):
                        print("Unzipping:", file);
                        z_ref = zipfile.ZipFile(os.path.join(root_path, file_path, file))
                        unz_path = os.path.join(root_path, temp_path, "".join(file.split(".")[:-1]))
                        z_ref.extractall()
                        z_ref.close();
                        print("Unzipped to", unz_path, ", editting")
                        source_path = os.path.join(unz_path, "OEBPS")
                        for pagefile in os.listdir(source_path):
                                if pagefile_re.match(pagefile):
                                        print("Editting", pagefile)
                                        freader = open(os.path.join(source_path, pagefile), 'r', encoding="utf8")
                                        text = freader.read()
                                        freader.close()
                                        fwriter = open(os.path.join(source_path, pagefile), 'w', encoding="utf8")
                                        fwriter.write(re.sub(error_re, "<br/>", text))
                                        fwriter.close()
                        print("Editted, rezipping")
                        targ_path = os.path.join(root_path, comp_path)
                        if not os.path.exists(targ_path):
                                os.mkdirs(targ_path)
                        shutil.make_archive(os.path.join(targ_path, file), 'zip', root_dir=unz_path, base_dir="./")
                        shutil.move(os.path.join(targ_path, file + ".zip"), os.path.join(targ_path, file))
                        print("Finished fixing", file, "placed at", targ_path)


if __name__ == "__main__":
        fix()
