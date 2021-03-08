from antlr4 import *

from gen.JavaLexer import JavaLexer
from gen.JavaParserLabeled import JavaParserLabeled
from gen.JavaParserLabeledListener import JavaParserLabeledListener


class ClassNameListener(JavaParserLabeledListener):
    def enterClassDeclaration(self, ctx: JavaParserLabeled.ClassDeclarationContext):
        print(f"Entered {ctx.IDENTIFIER().getText()} Class.")

    def exitClassDeclaration(self, ctx:JavaParserLabeled.ClassDeclarationContext):
        print(f"Exited {ctx.IDENTIFIER()} Class.")


if __name__ == '__main__':
    file_path = "C:\\Users\\RGY\\PycharmProjects\\compiler992\\test_project\\demo\\src\\main\\java\\com\\jsoniter\\demo\\Demo.java"
    stream = FileStream(file_path)
    lexer = JavaLexer(stream)
    tokens = CommonTokenStream(lexer)
    parser = JavaParserLabeled(tokens)
    tree = parser.compilationUnit()
    listener = ClassNameListener()
    walker = ParseTreeWalker()
    walker.walk(
        listener=listener,
        t=tree
    )
