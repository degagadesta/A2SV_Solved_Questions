class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_map = defaultdict(list)

        for path in paths:
            i = 0
            root_chars = []
            while i < len(path) and path[i] != " ":
                root_chars.append(path[i])
                i += 1
            root = "".join(root_chars)

            while i < len(path):
                while i < len(path) and path[i] == " ":
                    i += 1
                if i >= len(path):
                    break

                filename_chars = []
                while i < len(path) and path[i] != "(":
                    filename_chars.append(path[i])
                    i += 1
                filename = "".join(filename_chars)

                i += 1  
                content_chars = []
                while i < len(path) and path[i] != ")":
                    content_chars.append(path[i])
                    i += 1
                content = "".join(content_chars)
                i += 1  

                full_path = root + "/" + filename
                content_map[content].append(full_path)

        result = []
        for files in content_map.values():
            if len(files) > 1:
                result.append(files)

        return result
