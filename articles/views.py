from articles.http.request.article_create_data import (
    ArticleCreateData,
)
from rest_framework.response import (
    Response,
)
from rest_framework import (
    status,
    viewsets,
)
from articles.domain.article.article_criteria import (
    ArticleCriteria,
)
from articles.domain.article.article_update_data import (
    ArticleUpdateData,
)
from articles.domain.article_transformer import (
    ArticleTransformer,
)
from articles.http.request.article_create_request_validator import (
    ArticleCreateRequestValidator,
)
from articles.use_case.article_create_use_case import (
    ArticleCreateUseCase,
)
from articles.use_case.article_delete_use_case import (
    ArticleDeleteUseCase,
)
from articles.use_case.article_find_use_case import (
    ArticleFindUseCase,
)
from articles.use_case.article_search_use_case import (
    ArticleSearchUseCase,
)
from articles.use_case.article_update_use_case import (
    ArticleUpdateUseCase,
)


# MEMO: 可読性のため、viewにはメソッドをCRUD順に記述(単純なCRUD以外のエンドポイントがある場合はCRUDの次に記述)し、以降はプライベートメソッドやフレームワーク固有のオーバーライドメソッド等を記述する
class ArticleView(viewsets.ModelViewSet):
    def create(self, request, *args, **kwargs):
        validated_article_create_data = ArticleCreateRequestValidator().do_validate(
            request.data
        )

        article = ArticleCreateUseCase().create(validated_article_create_data)

        # MEMO: ドメイン層のオブジェクトをシリアライズ(配列や辞書に変換)する責務
        article = ArticleTransformer.to_dictionary(article)

        return Response(
            article,
            status=status.HTTP_201_CREATED,
        )

    def list(self, request, *args, **kwargs):
        # 例えば、著者名、タイトルで検索したい場合
        author_ids = request.query_params.get(
            "author_ids",
            [],
        )
        title = request.query_params.get(
            "title",
            "",
        )

        # MEMO: クエリパラメーターによるテーブルの条件検索には、criteriaパターンを使用する
        articles = ArticleSearchUseCase().search(
            ArticleCriteria().set_author_ids(author_ids).set_title(title)
        )

        articles = ArticleTransformer.to_array(articles)

        return Response(
            articles,
            status=status.HTTP_200_OK,
        )

    def retrieve(self, request, *args, **kwargs):
        id = kwargs["pk"]
        article = ArticleFindUseCase().find(id=id)
        article = ArticleTransformer.to_dictionary(article)

        return Response(
            article,
            status=status.HTTP_200_OK,
        )

    def update(self, request, *args, **kwargs):
        article = ArticleUpdateUseCase().update(
            ArticleUpdateData(
                id=request.data["id"],
                title=request.data["title"],
                content=request.data["content"],
                author_id=request.data["author_id"],
                tags=request.data["tags"],
                meta_title=request.data["meta_title"],
                meta_description=request.data["meta_description"],
            ),
        )

        article = ArticleTransformer.to_dictionary(article)

        return Response(
            article,
            status=status.HTTP_200_OK,
        )

    def destroy(self, request, *args, **kwargs):
        ArticleDeleteUseCase().delete(id=kwargs["pk"])
        return Response(status=status.HTTP_204_NO_CONTENT)
